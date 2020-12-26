import {Player} from "../model/player";
import React from "react";
import {createStyles, fade, makeStyles, Theme} from "@material-ui/core/styles";
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import Typography from "@material-ui/core/Typography";
import {Badge, Grid, Icon, Paper} from "@material-ui/core";
import TimeAgo from 'timeago-react';

interface IProps {
    classes: any
    players: Array<Player>
    firstPlayer: number,
    searching: boolean
}

const useStyles = makeStyles((theme: Theme) => createStyles({
    header: {
        padding: "0 0 1% 0",
        backgroundColor: theme.palette.background.paper,
    },
    titleText: {
        fontFamily: "Bebas Neue",
        fontSize: "6rem",
        textAlign: "center",
        height: "110px",
    },
    subheading: {
        textAlign: "center",
        color: theme.palette.text.secondary,
    },
    search: {
        position: "relative",
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        "&:hover": {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        width: "25%",
        margin: "auto",
        marginTop: "20px",
        border: "1px solid",
        borderColor: "rgba(255, 255, 255, 0.12)",
    },
    searchIcon: {
        padding: theme.spacing(0, 2),
        height: "100%",
        position: "absolute",
        pointerEvents: "none",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },
    inputRoot: {
        width: "100%",
        color: "inherit",
    },
    input: {
        padding: theme.spacing(1, 1, 1, 0),
        paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
        transition: theme.transitions.create("width"),
    },
    grid: {
        width: "60%",
        margin: "auto",
        padding: "20px",
    },
    paper: {
        height: "142px",
        borderRadius: "7px",
        textAlign: 'center',
        padding: theme.spacing(2),
        color: theme.palette.text.primary,
        "&:hover": {
            borderColor: theme.palette.primary.main
        }
    },
    avatar: {
        width: "55px",
        height: "55px",
        borderRadius: "55px",
        marginBottom: theme.spacing(1),
    },
    dateText: {
        paddingBottom: "2px",
        fontSize: "14px",
        color: theme.palette.text.secondary,
    },
    calendarIcon: {
        paddingTop: "1px",
        marginRight: "4px",
        fontSize: "14px",
        color: theme.palette.text.secondary,
    },
    rootBadge: {
        display: "block",
    }
}));

class LandingView extends React.Component<IProps> {
    render() {
        const classes = this.props.classes
        const players = this.props.players
        return (
            <div>
                <div className={classes.header}>
                    <Typography className={classes.titleText}>
                        Classes.gg
                    </Typography>
                    <Typography className={classes.subheading}>
                        Warzone Loadout Repository
                    </Typography>
                    <SearchField classes={classes} />
                </div>
                <div>
                    <Grid container className={classes.grid} spacing={3}>
                        {players.map((player: Player) => (
                            <Grid item xs={6} lg={2} key={player.username} className={classes.rootPaper}>
                                <Badge color="primary" badgeContent={player.nLoadouts}  classes={{root: classes.rootBadge}}>
                                    <Paper className={classes.paper} variant="outlined">
                                        <img className={classes.avatar} src={player.avatar} alt="" />
                                        <Typography>
                                            {player.username}
                                        </Typography>
                                        <Icon className={classes.calendarIcon}>calendar_today</Icon>
                                        <TimeAgo
                                            className={classes.dateText}
                                            datetime={player.lastUpdated}
                                        />
                                    </Paper>
                                </Badge>
                            </Grid>
                        ))}
                    </Grid>
                </div>
            </div>
        )
    }
}

const SearchField = (props: any) => {
    const classes = props.classes
    return (
        <div className={classes.search}>
            <div className={classes.searchIcon}>
                <SearchIcon />
            </div>
            <InputBase
                placeholder="Search for a player or loadout"
                classes={{
                    root: classes.inputRoot,
                    input: classes.input,
                }}
                // onChange={(event) => props.onSearch(event.target.value.toLowerCase())}
            />
        </div>
    )
}

export default (props: any) => {
    const classes = useStyles()
    return <LandingView
        classes={classes}
        players={props.players}
        firstPlayer={props.firstPlayer}
        searching={props.searching}
    />
}
