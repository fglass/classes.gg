import React from "react";
import Slider, { LazyLoadTypes } from "react-slick";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import PlayerCard from "./PlayerCard";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "../model/player";
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";

interface IProps {
    classes: any
    players: Array<Player>
    firstPlayer: number,
    searching: boolean
}

const useStyles = makeStyles(theme => ({
    container: {
        minHeight: 348,
        maxHeight: 348,
        [theme.breakpoints.down("sm")]: {
            minHeight: 329,
            maxHeight: 329,
        },
        paddingTop: theme.spacing(5),
        paddingBottom: theme.spacing(5),
        backgroundColor: theme.palette.background.paper,
    },
    emptyContainer: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: 348,
        maxHeight: 348,
        [theme.breakpoints.down("sm")]: {
            minHeight: 329,
            maxHeight: 329,
        },
        backgroundColor: theme.palette.background.paper,
    },
    noMatches: {
        height: "100%",
        fontFamily: "Bebas Neue",
        fontSize: "5rem",
        opacity: "50%"
    },
}));

function getSlidesForWidth(width: number) {
    if (width <= 600) { // xs
        return 1
    }
    const cardWidth = 310;
    return Math.floor(width / cardWidth);
}

function Arrow(props: any) {
    const { className, existingStyle, onClick, next, offset } = props
    const style = next ? { ...existingStyle, right: offset } : { ...existingStyle, left: offset, zIndex: 1 }
    return (
        <div
            className={className}
            style={style}
            onClick={onClick}
        />
    );
}

const sliderSettings = {
    initialSlide: 0,
    slidesToShow: 5,
    slidesToScroll: 5,
    speed: 400,
    prevArrow: <Arrow offset={8} />,
    nextArrow: <Arrow offset={8} next />,
    lazyLoad: "progressive" as LazyLoadTypes,
    responsive: [
        {
            breakpoint: 600, // xs
            settings: {
                slidesToShow: getSlidesForWidth(600),
                slidesToScroll: getSlidesForWidth(600),
                prevArrow: <Arrow offset={"5%"} />,
                nextArrow: <Arrow offset={"5%"} next />,
                swipeToSlide: true,
            }
        }
    ]
};

const SliderView = (props: any) => {
    const { className, players } = props
    return (
        <div className={className}>
            <Slider {...sliderSettings}>
                {players.map((player: Player) => (
                    <div key={player.username}>
                        <PlayerCard
                            username={player.username}
                            avatar={player.avatar}
                        />
                    </div>
                ))}
            </Slider>
        </div>
    )
}

const StaticView = (props: any) => {
    const { className, players } = props
    return (
        <div className={className}>
            <Grid container>
                {players.map((player: Player) => (
                    <Grid item xs key={player.username}>
                        <PlayerCard
                            username={player.username}
                            avatar={player.avatar}
                        />
                    </Grid>
                ))}
            </Grid>
        </div>
    )
}

class SelectionView extends React.Component<IProps> {

    resize = () => this.forceUpdate()

    componentDidMount() {
        window.addEventListener("resize", this.resize) // Redraw on resize
    }

    componentWillUnmount() {
        window.removeEventListener("resize", this.resize)
    }

    render() {
        const { classes, players, firstPlayer, searching } = this.props

        if (searching && players.length === 0) {
            return (
                <div className={classes.emptyContainer}>
                    <Typography className={classes.noMatches} align="center">
                        No Matches
                    </Typography>
                </div>
            )
        }

        const slides = getSlidesForWidth(window.innerWidth);

        if (players.length > slides) {
            // Update dynamic config
            sliderSettings["slidesToShow"] = slides
            sliderSettings["slidesToScroll"] = slides
            sliderSettings["initialSlide"] = firstPlayer
            return <SliderView className={classes.container} players={players} />
        } else {
            return <StaticView className={classes.container} players={players} />
        }
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <SelectionView
        classes={classes}
        players={props.players}
        firstPlayer={props.firstPlayer}
        searching={props.searching}
    />
}