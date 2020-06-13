import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Footer from "./Footer";
import Header from "./Header";
import LandingPage from "./LandingPage";
import { blue } from '@material-ui/core/colors';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';

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
                <CssBaseline />
                <Header />
                <LandingPage />
                <Footer />
            </ThemeProvider>
        </React.Fragment>
    );
}
