import React from 'react';
import ReactGA from 'react-ga';
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
}

export default class App extends React.Component<any, IState> {

    private static ANALYTICS_TRACKING_CODE = "UA-131273827-2"

    constructor(props: any) {
        super(props);
        this.state = {
            players: [],
            filteredPlayers: [],
        }
    }

    async getPlayers() {
        const players = await Api.getPlayers()
        this.setState({
            players,
            filteredPlayers: players,
        })
    }

    componentDidMount() {
        ReactGA.initialize(App.ANALYTICS_TRACKING_CODE)
        ReactGA.pageview(window.location.pathname + window.location.search)
        this.getPlayers().catch(err => console.log(err))
    }

    onSearch = (input: string) => {
        this.setState({
            filteredPlayers: this.state.players.filter(player => player.username.toLowerCase().startsWith((input)))
        })
    }

    selectPlayer = (username: string) => {
        const suffix = `/${username}`
        window.history.pushState({urlPath: suffix}, "", suffix) // Update URL
        this.forceUpdate()
    }

    render() {
        const { players, filteredPlayers } = this.state
        return (
            <React.Fragment>
                <ThemeProvider theme={darkTheme}>
                    <CssBaseline />
                    <Header onSearch={this.onSearch} />
                    <SelectionView
                        players={filteredPlayers}
                        searching={players.length !== filteredPlayers.length}
                        selectPlayer={this.selectPlayer}
                    />
                    {players.length > 0 &&
                        <PlayerView username={window.location.pathname.replace("/", "") || players[0].username} />
                    }
                    <Footer />
                </ThemeProvider>
            </React.Fragment>
        );
    }
}