import React from "react";
import Slider from "react-slick";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import PlayerCard from "./PlayerCard";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "../domain/player";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

interface IProps {
    classes: any
    players: Array<Player>
    selectPlayer: (username: string) => void
    searching: boolean
}

const useStyles = makeStyles(theme => ({
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: 407,
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
        backgroundColor: theme.palette.background.paper,
    },
    noMatches: {
        height: '100%',
        fontFamily: 'Bebas Neue',
        fontSize: '5rem',
        opacity: '50%'
    },
}));

function getSlidesForWidth(width: number) {
    if (width <= 600) {             // xs
        return 1
    } else if (width <= 960) {      // sm
        return 3
    } else if (width <= 1280) {     // md
        return 4
    }
    return 5;
}

function Arrow(props: any) {
    const { className, existingStyle, onClick, next } = props;
    const style = next ? { ...existingStyle, right: '5%' } : { ...existingStyle, left: '5%', zIndex: 1 }
    return (
        <div
            className={className}
            style={style}
            onClick={onClick}
        />
    );
}

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
                slidesToShow: getSlidesForWidth(1280),
            }
        },
        {
            breakpoint: 960, // sm
            settings: {
                slidesToShow: getSlidesForWidth(960),
            }
        },
        {
            breakpoint: 600, // xs
            settings: {
                slidesToShow: getSlidesForWidth(600),
                prevArrow: <Arrow />,
                nextArrow: <Arrow next />,
                arrows: true,
                swipe: true,
                swipeToSlide: true,
                autoplay: false,
                speed: 250,
            }
        }
    ]
};

class SelectionView extends React.Component<IProps> {

    resize = () => this.forceUpdate()

    componentDidMount() {
        window.addEventListener("resize", this.resize) // In case static view required after resize
    }

    componentWillUnmount() {
        window.removeEventListener("resize", this.resize)
    }

    render() {
        const { classes, players, selectPlayer, searching } = this.props

        if (searching && players.length === 0) {
            return(
                <div className={classes.container}>
                    <Typography className={classes.noMatches} align="center">
                        No Matches
                    </Typography>
                </div>
            )
        }

        const isCarousel = players.length > getSlidesForWidth(window.innerWidth) // Sliding required

        const cards = players.map((player) => (
            <div key={player.username}>
                <PlayerCard
                    username={player.username}
                    avatar={player.avatar}
                    selectPlayer={selectPlayer}
                />
            </div>
        ))

        return isCarousel ? (
            <Slider className={classes.container} {...sliderSettings}>
                {cards}
            </Slider>
        ) : (
            <div className={classes.container}>
                <Grid container>
                    {cards.map((card, index) => (
                        <Grid item xs key={index}>
                            {card}
                        </Grid>
                    ))}
                </Grid>
            </div>
        )
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <SelectionView
        classes={classes}
        players={props.players}
        selectPlayer={props.selectPlayer}
        searching={props.searching}
    />
}