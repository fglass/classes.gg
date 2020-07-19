import React from "react";
import ReactGA from "react-ga";
import Api from "../model/api";
import CssBaseline from "@material-ui/core/CssBaseline";
import Content from "./Content";
import Footer from "./Footer";
import Header from "./Header";
import { blue } from "@material-ui/core/colors";
import { createMuiTheme, makeStyles, ThemeProvider } from "@material-ui/core/styles";
import { Player } from "../model/player";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Helmet } from "react-helmet";

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
        type: "dark",
    },
});

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
    },
    main: {
        display: "flex",
        flexGrow: 1,
        justifyContent: "center",
        alignItems: "center",
        [theme.breakpoints.up("md")]: {
            marginTop: theme.spacing(5),
            marginBottom: theme.spacing(5),
        }
    },
}));

const HelmetHead = (props: any) => {
    const player = props.player
    let title = "Classes.gg - Warzone Loadout Repository"
    let description = "View Call of Duty: Warzone loadouts of professional players, streamers and other content creators"

    if (player) {
        title = `Classes.gg - ${player} Warzone Loadouts`
        description = `View Call of Duty: Warzone loadouts of ${player}`
    }

    return (
        <Helmet>
            <title>{title}</title>
            <meta name="description" content={description} />
        </Helmet>
    )
}

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

    render() {
        const { classes } = this.props
        const { players, filteredPlayers } = this.state


        if (players.length === 0) {
            return <div className={classes.main} />
        }

        return (
            <Router>
                <div className={classes.root} >
                    <ThemeProvider theme={darkTheme}>
                        <CssBaseline />
                        <Header onSearch={this.onSearch} />
                        <Switch>
                            <Route path="/:player?" render={(props) =>
                                (
                                    <React.Fragment>
                                        <HelmetHead player={props.match.params.player} />
                                        <Content
                                            className={classes.main}
                                            players={filteredPlayers}
                                            username={props.match.params.player || players[0].username}
                                            searching={players.length !== filteredPlayers.length}
                                        />
                                    </React.Fragment>
                                )
                            }>
                            </Route>
                        </Switch>
                        <Footer />
                    </ThemeProvider>
                </div>
            </Router>
        );
    }
}

export default () => {
    const classes = useStyles()
    return <App classes={classes}/>
}