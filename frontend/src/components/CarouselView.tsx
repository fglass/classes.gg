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
        backgroundColor: theme.palette.background.paper,
    }
}));

const sliderSettings = {
    slidesToShow: 5,
    pauseOnHover: false,
    swipe: false,
    arrows: false,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 100,
    speed: 2000,
    responsive: [
        {
            breakpoint: 1280, // md
            settings: {
                slidesToShow: 4,
            }
        },
        {
            breakpoint: 960, // sm
            settings: {
                slidesToShow: 3,
            }
        },
        {
            breakpoint: 600, // xs
            settings: {
                slidesToShow: 1,
                swipe: true,
                swipeToSlide: true,
                autoplay: false,
                speed: 0,
            }
        }
    ]
};

class CarouselView extends React.Component<IProps> {

    render() {
        const { classes, players } = this.props
        const n = players.length

        const cards = this.props.players.map((player) => (
            <div key={player.username}>
                <PlayerCard
                    username={player.username}
                    avatar={player.avatar}
                    selectPlayer={this.props.selectPlayer}
                />
            </div>
        ))

        const isCarousel= n > 5 // TODO: replace 5

        return isCarousel ? (
            <Slider className={classes.container} {...sliderSettings}>
                {cards}
            </Slider>
        ) : (
            <div className={classes.container}>
                {cards}
            </div>
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