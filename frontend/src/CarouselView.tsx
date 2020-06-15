import React from "react";
import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Slider from "react-slick";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "./player";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

// TODO: https://mui-treasury.com/components/card/

const useStyles = makeStyles(theme => ({
    cardGrid: {
        paddingTop: theme.spacing(8),
        paddingLeft: theme.spacing(8),
        paddingRight: theme.spacing(8),
        paddingBottom: theme.spacing(8),
    },
    card: {
        maxWidth: 260,
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
        const settings = {
            infinite: true,
            slidesToShow: 5,
            autoplay: true,
            autoplaySpeed: 100,
            speed: 2000,
        };
        return (
            <Slider className={classes.cardGrid} {...settings}>
                {this.state.players.map((player, index) => (
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
                        </CardContent>
                        <CardActions>
                            <Button href={`/player/${player.username}`} size="small" variant="contained" color="primary">
                                View
                            </Button>
                        </CardActions>
                    </Card>
                ))}
            </Slider>
        )
    }
}

export default () => {
    const classes = useStyles()
    return <CarouselView classes={classes} />
}