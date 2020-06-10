import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import ClassSharpIcon from '@material-ui/icons/ClassSharp';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { createMuiTheme, ThemeProvider, makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { lightBlue } from "@material-ui/core/colors";

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary">
            {new Date().getFullYear()}
            {' © FG.'}
        </Typography>
    );
}

const darkTheme = createMuiTheme({
    palette: {
        primary: lightBlue,
        type: 'dark',
    },
});

const useStyles = makeStyles({
    icon: {
        marginRight: darkTheme.spacing(2),
    },
    heroContent: {
        backgroundColor: darkTheme.palette.background.paper,
        padding: darkTheme.spacing(8, 0, 6),
    },
    heroButtons: {
        marginTop: darkTheme.spacing(4),
    },
    cardGrid: {
        paddingTop: darkTheme.spacing(8),
        paddingBottom: darkTheme.spacing(8),
    },
    card: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
    },
    cardMedia: {
        paddingTop: '56.25%', // 16:9
    },
    cardContent: {
        flexGrow: 1,
    },
    footer: {
        backgroundColor: darkTheme.palette.background.paper,
        padding: darkTheme.spacing(6),
    },
});

const cards = [1, 2, 3, 4, 5, 6];

export default function App() {
    const classes = useStyles();
    return (
        <React.Fragment>
            <ThemeProvider theme={darkTheme}>
                <CssBaseline />
                <AppBar position="relative">
                    <Toolbar>
                        <ClassSharpIcon className={classes.icon} />
                    </Toolbar>
                </AppBar>
                <main>
                    {/* Hero unit */}
                    <div className={classes.heroContent}>
                        <Container maxWidth="sm">
                            <Typography component="h1" variant="h2" align="center" color="textPrimary" gutterBottom>
                                Classes.gg
                            </Typography>
                            <Typography variant="h5" align="center" color="textSecondary" paragraph>
                                Discover which Warzone loadouts pro players and content creators are currently using.
                            </Typography>
                            <div className={classes.heroButtons}>
                                <Grid container spacing={2} justify="center">
                                    <Grid item>
                                        <Button variant="contained" color="primary">
                                            Browse
                                        </Button>
                                    </Grid>
                                    <Grid item>
                                        <Button variant="outlined" color="primary">
                                            Random
                                        </Button>
                                    </Grid>
                                </Grid>
                            </div>
                        </Container>
                    </div>
                    <Container className={classes.cardGrid} maxWidth="md">
                        {/* End hero unit */}
                        <Grid container spacing={4}>
                            {cards.map((card) => (
                                <Grid item key={card} xs={12} sm={6} md={4}>
                                    <Card className={classes.card}>
                                        <CardMedia
                                            className={classes.cardMedia}
                                            image="https://source.unsplash.com/random"
                                            title="Image title"
                                        />
                                        <CardContent className={classes.cardContent}>
                                            <Typography gutterBottom variant="h5" component="h2">
                                                Streamer {card}
                                            </Typography>
                                            <Typography>
                                                This is the loadout of streamer {card}
                                            </Typography>
                                        </CardContent>
                                        <CardActions>
                                            <Button size="small" color="primary">
                                                View
                                            </Button>
                                        </CardActions>
                                    </Card>
                                </Grid>
                            ))}
                        </Grid>
                    </Container>
                </main>
                {/* Footer */}
                <footer className={classes.footer}>
                    <Copyright />
                    <Typography variant="body2" color="textSecondary" component="p">
                        Activision has not endorsed and is not responsible for this site or its content.
                    </Typography>
                </footer>
                {/* End footer */}
            </ThemeProvider>
        </React.Fragment>
    );
}
