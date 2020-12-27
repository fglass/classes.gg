import React from "react";
import Api from "../model/api";
import PlayerView from "./PlayerView";
import { Player } from "../model/player";

interface IProps {
    className: string
    username: string
}

interface IState {
    selectedPlayer: Player | null
}

export default class Content extends React.Component<IProps, IState> { // TODO: merge with playter view

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
        const { className } = this.props
        const selectedPlayer = this.state.selectedPlayer

        if (selectedPlayer === null) {
            return <div className={className} />
        }

        return (
            <div className={className}>
                 <PlayerView player={selectedPlayer} />
            </div>
        )
    }
}
