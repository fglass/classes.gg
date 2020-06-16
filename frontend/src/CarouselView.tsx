import React from "react";
import Slider from "react-slick";
import PlayerCard from "./PlayerCard";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "./player";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

interface IProps {
    classes: any
}

interface IState {
    players: Array<Player>
}

const useStyles = makeStyles(theme => ({
    container: {
        paddingTop: theme.spacing(8),
        paddingRight: theme.spacing(8),
        paddingLeft: theme.spacing(8),
        paddingBottom: theme.spacing(8),
    },
}));

class CarouselView extends React.Component<IProps, IState> {
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
        const settings = {
            infinite: true,
            slidesToShow: 5,
            autoplay: true,
            autoplaySpeed: 100,
            speed: 2000,
        };
        return (
            <Slider className={classes.container} {...settings}>
                {this.state.players.map((player) => (
                    <PlayerCard
                        avatar={player.avatar}
                        username={player.username}
                    />
                ))}
            </Slider>
        )
    }
}

export default () => {
    const classes = useStyles()
    return <CarouselView classes={classes} />
}