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
    firstPlayer: number,
    selectPlayer: (username: string) => void
    searching: boolean
}

const useStyles = makeStyles(theme => ({
    container: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: 359,
        paddingTop: theme.spacing(5),
        paddingBottom: theme.spacing(5),
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
    if (width <= 600) { // xs
        return 1
    }
    const cardWidth = 300;
    return Math.floor(width / cardWidth);
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
    initialSlide: 0,
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
        const { classes, players, firstPlayer, selectPlayer, searching } = this.props

        if (searching && players.length === 0) {
            return(
                <div className={classes.container}>
                    <Typography className={classes.noMatches} align="center">
                        No Matches
                    </Typography>
                </div>
            )
        }

        let view;

        const slides = getSlidesForWidth(window.innerWidth);

        // Carousel view
        if (players.length > slides) {

            sliderSettings["slidesToShow"] = slides // Dynamic number of slides

            if (slides === 1) {
                sliderSettings["initialSlide"] = firstPlayer // Mobile only
            }

            view = (
                <Slider className={classes.container} {...sliderSettings}>
                    {players.map((player) => (
                        <div key={player.username}>
                            <PlayerCard
                                username={player.username}
                                avatar={player.avatar}
                                selectPlayer={selectPlayer}
                            />
                        </div>
                    ))}
                </Slider>
            )

        // Static view
        } else {
            view = (
                <div className={classes.container}>
                    <Grid container>
                        {players.map((player) => (
                            <Grid item xs key={player.username}>
                                <PlayerCard
                                    username={player.username}
                                    avatar={player.avatar}
                                    selectPlayer={selectPlayer}
                                />
                            </Grid>
                        ))}
                    </Grid>
                </div>
            )
        }

        return view;
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <SelectionView
        classes={classes}
        players={props.players}
        firstPlayer={props.firstPlayer}
        selectPlayer={props.selectPlayer}
        searching={props.searching}
    />
}