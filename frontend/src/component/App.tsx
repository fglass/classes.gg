import React from "react";
import ReactGA from "react-ga";
import Api from "../model/api";
import CssBaseline from "@material-ui/core/CssBaseline";
import Footer from "./Footer";
import Header from "./Header";
import LandingView from "./landing/LandingView";
import PlayerView from "./player/PlayerView";
import { blue } from "@material-ui/core/colors";
import { createMuiTheme, makeStyles, ThemeProvider } from "@material-ui/core/styles";
import { Player } from "../model/player";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import {SEO} from "./SEO";

interface IProps {
    classes: any
}

interface IState {
    players: Array<Player>
}

const darkTheme = createMuiTheme({
    palette: {
        primary: blue,
        type: "dark",
    },
    overrides: {
        MuiExpansionPanel: {
            root: {
                "&$expanded": {
                    "&:last-child": {
                        marginBottom: "10px"
                    }
                }
            }
        },
        MuiExpansionPanelSummary: {
            root: {
                "&$expanded": {
                    minHeight: "none"
                }
            }
        }
    }
});

const useStyles = makeStyles((theme) => ({
    root: {
        position: "relative",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
    },
    main: {
        display: "flex",
        flexGrow: 1,
        justifyContent: "center",
        alignItems: "center",
        [theme.breakpoints.up("md")]: {
            marginTop: theme.spacing(3),
            marginBottom: theme.spacing(3),
        }
    },
}));

class App extends React.Component<IProps, IState> {

    private static ANALYTICS_TRACKING_CODE = "UA-131273827-2"
    private static CREATION_DATE = "2020-07-03T00:00:00.000000"

    constructor(props: IProps) {
        super(props);
        this.state = {
            players: [],
        }
    }

    async getPlayers() {
        const players = await Api.getPlayers()
        this.setState({
            players,
        })
    }

    componentDidMount() {
        if (process.env.NODE_ENV === "production") {
            ReactGA.initialize(App.ANALYTICS_TRACKING_CODE)
            ReactGA.pageview(window.location.pathname + window.location.search)
        }
        this.getPlayers().catch(err => console.log(err))
    }

    render() {
        const classes = this.props.classes
        const players = this.state.players
        return (
            <Router>
                <div className={classes.root} >
                    <ThemeProvider theme={darkTheme}>
                        <CssBaseline />
                        <Header />
                        <Switch>
                            <Route path="/:username" render={(props) => (
                                <React.Fragment>
                                    <SEO username={props.match.params.username} date={App.CREATION_DATE} />
                                    <PlayerView
                                        className={classes.main}
                                        player={players.find(player => player.username === props.match.params.username)}
                                    />
                                </React.Fragment>
                            )}>
                            </Route>
                            <Route>
                                <SEO username="" date={App.CREATION_DATE} />
                                <LandingView players={players} />
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