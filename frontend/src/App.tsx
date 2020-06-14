import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Footer from "./Footer";
import Header from "./Header";
import CarouselView from "./CarouselView";
import PlayerView from "./PlayerView";
import { blue } from '@material-ui/core/colors';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { BrowserRouter as Router, Switch, Route }from "react-router-dom";

const darkTheme = createMuiTheme({
    palette: {
        primary: blue,
        type: 'dark',
    },
});

export default function App() {
    return (
        <React.Fragment>
            <ThemeProvider theme={darkTheme}>
                <Router>
                    <CssBaseline />
                    <Header />
                    <Switch>
                        <Route path="/player">
                            <PlayerView />
                        </Route>
                        <Route path="/">
                            <CarouselView />
                        </Route>
                    </Switch>
                    <Footer />
                </Router>
            </ThemeProvider>
        </React.Fragment>
    );
}
