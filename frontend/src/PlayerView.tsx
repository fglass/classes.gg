import React from "react";
import { useParams } from "react-router";
import { Player } from "./player";

interface IProps {
    username: string
}

interface IState {
    player: Player | null
}

class PlayerView extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            player: null
        }
    }

    async http<T>(request: string): Promise<T> {
        const response = await fetch(request);
        return await response.json();
    }

    async queryPlayer() {
        const player = await this.http<Player>(`http://localhost:5000/player/${this.props.username}`)
        this.setState({player})
    }

    componentDidMount() {
        this.queryPlayer()
    }

    render() {
        const player = this.state.player

        if (player == null) {
            return null
        }

        return (
            <div>
                <h2>{player.username}</h2>
                {Object.entries(player.weapons).map((weapon) => {
                    const [name, attachments] = weapon;
                    return (
                        <h3>{name}: {attachments.join(", ")}</h3>
                    )
                })}
            </div>
        );
    }
}

export default () => {
    const { username } = useParams();
    return (
        <PlayerView username={username} />
    )
}