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
import {Link} from "react-router-dom";

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

class CarouselView extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            players: []
        }
    }

    capitalise = (s: any) => {
        if (typeof s !== 'string') return ''
        return s.charAt(0).toUpperCase() + s.slice(1)
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
                                    image={player.avatar}
                                    title=""
                                />
                                <CardContent className={classes.cardContent}>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {this.capitalise(player.username)}
                                    </Typography>
                                    <Typography>
                                        {Object.keys(player.weapons).join(", ")}
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Link to={`/player/${player.username}`}>
                                        <Button size="small" variant="contained" color="primary">
                                            View
                                        </Button>
                                    </Link>
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
        <CarouselView classes={classes} />
    )
}