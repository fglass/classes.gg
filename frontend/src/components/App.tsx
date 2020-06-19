import React from 'react';
import Api from "../domain/api";
import CssBaseline from '@material-ui/core/CssBaseline';
import Footer from "./Footer";
import Header from "./Header";
import CarouselView from "./CarouselView";
import PlayerView from "./PlayerView";
import { blue } from '@material-ui/core/colors';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import {Player} from "../domain/player";

const darkTheme = createMuiTheme({
    palette: {
        primary: blue,
        type: 'dark',
    },
});

interface IState {
    players: Array<Player>
    selectedPlayer: string
}

export default class App extends React.Component<any, IState> {
    constructor(props: any) {
        super(props);
        this.state = {
            players: [],
            selectedPlayer: "Unknown"
        }
    }

    async getPlayers() {
        const players = await Api.getPlayers()
        this.setState({
            players,
            selectedPlayer: players[0].username
        })
    }

    componentDidMount() {
        this.getPlayers().catch(err => console.log(err))
    }

    selectPlayer = (username: string) => {
        this.setState({selectedPlayer: username})
    };

    render() {
        return (
            <React.Fragment>
                <ThemeProvider theme={darkTheme}>
                    <CssBaseline />
                    <Header />
                    <CarouselView players={this.state.players} selectPlayer={this.selectPlayer} />
                    <PlayerView username={this.state.selectedPlayer} />
                    <Footer />
                </ThemeProvider>
            </React.Fragment>
        );
    }
}