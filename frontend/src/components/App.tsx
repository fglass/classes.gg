import React from 'react';
import Api from "../domain/api";
import CssBaseline from '@material-ui/core/CssBaseline';
import Footer from "./Footer";
import Header from "./Header";
import SelectionView from "./SelectionView";
import PlayerView from "./PlayerView";
import { blue } from '@material-ui/core/colors';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { Player } from "../domain/player";

const darkTheme = createMuiTheme({
    palette: {
        primary: blue,
        type: 'dark',
    },
});

interface IState {
    players: Array<Player>
    filteredPlayers: Array<Player>
    selectedPlayer: string
}

export default class App extends React.Component<any, IState> {
    constructor(props: any) {
        super(props);
        this.state = {
            players: [],
            filteredPlayers: [],
            selectedPlayer: "Unknown"
        }
    }

    async getPlayers() {
        const players = await Api.getPlayers()
        this.setState({
            players,
            filteredPlayers: players,
            selectedPlayer: players[0].username
        })
    }

    componentDidMount() {
        this.getPlayers().catch(err => console.log(err))
    }

    selectPlayer = (username: string) => {
        this.setState({selectedPlayer: username})
    }

    onSearch = (input: string) => {
        this.setState({
            filteredPlayers: this.state.players.filter(player => player.username.toLowerCase().startsWith((input)))
        })
    }

    render() {
        return (
            <React.Fragment>
                <ThemeProvider theme={darkTheme}>
                    <CssBaseline />
                    <Header onSearch={this.onSearch} />
                    <SelectionView
                        players={this.state.filteredPlayers}
                        selectPlayer={this.selectPlayer}
                    />
                    <PlayerView username={this.state.selectedPlayer} />
                    <Footer />
                </ThemeProvider>
            </React.Fragment>
        );
    }
}