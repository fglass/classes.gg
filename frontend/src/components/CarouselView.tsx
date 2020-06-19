import React from "react";
import Slider from "react-slick";
import PlayerCard from "./PlayerCard";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "../domain/player";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

interface IProps {
    classes: any
    players: Array<Player>
    selectPlayer: (username: string) => void
}

const useStyles = makeStyles(theme => ({
    container: {
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
    },
}));

class CarouselView extends React.Component<IProps> {

    render() {
        const classes = this.props.classes;
        const settings = {
            slidesToShow: 5,
            arrows: false,
            infinite: true,
            autoplay: true,
            autoplaySpeed: 100,
            speed: 2000,
        };
        return (
            <Slider className={classes.container} {...settings}>
                {this.props.players.map((player) => (
                    <PlayerCard
                        key={player.username}
                        username={player.username}
                        avatar={player.avatar}
                        selectPlayer={this.props.selectPlayer}
                    />
                ))}
            </Slider>
        )
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <CarouselView
        classes={classes}
        players={props.players}
        selectPlayer={props.selectPlayer}
    />
}