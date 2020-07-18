import React from "react";
import Api from "../domain/api";
import SelectionView from "./SelectionView";
import PlayerView from "./PlayerView";
import { Player } from "../domain/player";

interface IProps {
    className: string
    players: Array<Player>
    username: string
    searching: boolean
}

interface IState {
    selectedPlayer: Player | null
}

export default class Content extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
        this.state = {
            selectedPlayer: null
        }
    }

    async getPlayer() {
        const selectedPlayer = await Api.getPlayer(this.props.username)
        this.setState({selectedPlayer})
    }

    componentDidMount() {
        this.getPlayer().catch(err => console.log(err))
    }

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.username !== prevProps.username) {
            this.getPlayer().catch(err => console.log(err))
        }
    }

    render() {
        const { className, players, searching } = this.props
        const selectedPlayer = this.state.selectedPlayer

        if (selectedPlayer === null) {
            return <div className={className} />
        }

        return (
            <React.Fragment>
                <SelectionView
                    players={players}
                    firstPlayer={players.findIndex(player => player.username === selectedPlayer.username)}
                    searching={searching}
                />
                <div className={className}>
                     <PlayerView player={selectedPlayer} />
                </div>
            </React.Fragment>
        )
    }
}