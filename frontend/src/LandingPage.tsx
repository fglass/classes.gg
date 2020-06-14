import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import {makeStyles} from "@material-ui/core/styles";
import {Player} from "./player";

const useStyles = makeStyles(theme => ({
    cardGrid: {
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
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
}));

interface IProps {
    classes: any
}

interface IState {
    players: Array<Player>
}

class LandingPage extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            players: []
        }
    }

    async http<T>(request: string): Promise<T> {
        const response = await fetch(request);
        return await response.json();
    }

    async queryPlayers() {
        const players = await this.http<Array<Player>>("http://localhost:5000/players")
        this.setState({players})
    }

    componentDidMount() {
        this.queryPlayers()
    }

    render() {
        const classes = this.props.classes;
        return (
            <Container className={classes.cardGrid} maxWidth="md">
                <Grid container spacing={4}>
                    {this.state.players.map((player, index) => (
                        <Grid item key={index} xs={12} sm={6} md={4}>
                            <Card className={classes.card}>
                                <CardMedia
                                    className={classes.cardMedia}
                                    image="https://static-cdn.jtvnw.net/jtv_user_pictures/9ea9d6d3-cc64-42e2-a66f-f74624ff81be-profile_image-300x300.png"
                                    title="Image title"
                                />
                                <CardContent className={classes.cardContent}>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {player.username}
                                    </Typography>
                                    <Typography>
                                        {Object.keys(player.weapons).join(", ")}
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size="small" variant="contained" color="primary">
                                        View
                                    </Button>
                                </CardActions>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </Container>
        )
    }
}

export default () => {
    const classes = useStyles()
    return (
        <LandingPage classes={classes} />
    )
}