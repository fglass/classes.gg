import React from 'react';
import ReactGA from 'react-ga';
import Api from "../domain/api";
import CssBaseline from '@material-ui/core/CssBaseline';
import Footer from "./Footer";
import Header from "./Header";
import SelectionView from "./SelectionView";
import PlayerView from "./PlayerView";
import { blue } from '@material-ui/core/colors';
import { createMuiTheme, makeStyles, ThemeProvider } from '@material-ui/core/styles';
import { Player } from "../domain/player";

interface IProps {
    classes: any
}

interface IState {
    players: Array<Player>
    filteredPlayers: Array<Player>
}

const darkTheme = createMuiTheme({
    palette: {
        primary: blue,
        type: 'dark',
    },
});

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
    },
    main: {
        display: 'flex',
        flexGrow: 1,
        justifyContent: 'center',
        alignItems: 'center',
        [theme.breakpoints.up('md')]: {
            marginTop: theme.spacing(5),
            marginBottom: theme.spacing(5),
        }
    },
}));

class App extends React.Component<IProps, IState> {

    private static ANALYTICS_TRACKING_CODE = "UA-131273827-2"

    constructor(props: IProps) {
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
        if (process.env.NODE_ENV === "production") {
            ReactGA.initialize(App.ANALYTICS_TRACKING_CODE)
            ReactGA.pageview(window.location.pathname + window.location.search)
        }
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
        const { classes } = this.props;
        const { players, filteredPlayers } = this.state

        let content = <div className={classes.main} />

        if (players.length > 0) {
            const selectedPlayer = window.location.pathname.replace("/", "") || players[0].username
            content = (
                <React.Fragment>
                    <SelectionView
                        players={filteredPlayers}
                        firstPlayer={players.findIndex(player => player.username === selectedPlayer)}
                        selectPlayer={this.selectPlayer}
                        searching={players.length !== filteredPlayers.length}
                    />
                    <div className={classes.main}>
                        <PlayerView username={selectedPlayer} />
                    </div>
                </React.Fragment>
            )
        }

        return (
            <div className={classes.root} >
                <ThemeProvider theme={darkTheme}>
                    <CssBaseline />
                    <Header onSearch={this.onSearch} />
                    {content}
                    <Footer />
                </ThemeProvider>
            </div>
        );
    }
}

export default () => {
    const classes = useStyles()
    return <App classes={classes}/>
}