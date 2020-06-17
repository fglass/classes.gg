import React from "react";
import Api from "./api";
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

    async getPlayer() {
        this.setState({player: await Api.getPlayer(this.props.username)})
    }

    componentDidMount() {
        this.getPlayer().catch(err => console.log(err))
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
    return <PlayerView username={username} />
}