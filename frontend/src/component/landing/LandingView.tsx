import React from "react";
import TimeAgo from 'timeago-react';
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import Typography from "@material-ui/core/Typography";
import { Badge, Icon, Paper } from "@material-ui/core";
import { Link } from "react-router-dom";
import { Player } from "../../model/player";
import { useStyles } from "./styles";

interface IProps {
    classes: any
    players: Array<Player>
}

interface IState {
    filteredPlayers: Array<Player>
}

class LandingView extends React.Component<IProps, IState> {

    constructor(props: IProps) {
        super(props);
        this.state = {
            filteredPlayers: this.props.players,
        }
    }

    onSearch = (input: string) => {
        this.setState({
            filteredPlayers: this.props.players.filter(player => player.username.toLowerCase().startsWith((input)))
        })
    }

    render() {
        const { classes } = this.props
        return (
            <div className={classes.content}>
                <div className={classes.header}>
                    <Typography className={classes.heading}>
                        Classes<span className={classes.primaryColour}>.</span>gg
                    </Typography>
                    <Typography className={classes.subheading}>
                        Call of Duty: Warzone Loadout Repository
                    </Typography>
                    <SearchField classes={classes} onSearch={this.onSearch} />
                </div>
                <div>
                    <div className={classes.grid}>
                        {
                            this.state.filteredPlayers.map((player: Player) =>
                            <PlayerCard classes={classes} player={player} key={player.username} />)
                        }
                    </div>
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
                onChange={(event) => props.onSearch(event.target.value.toLowerCase())}
            />
        </div>
    )
}

const PlayerCard = (props: any) => {
    const { classes, player } = props
    return (
        <div>
            <Badge color="primary" badgeContent={player.nLoadouts} >
                <Link to={`/${player.username}`}>
                    <Paper className={classes.card} variant="outlined">
                        <img className={classes.avatar} src={player.avatar} alt="" />
                        <Typography>{player.username}</Typography>
                        <Icon className={classes.calendarIcon}>calendar_today</Icon>
                        <TimeAgo
                            className={classes.timeAgo}
                            datetime={player.lastUpdated}
                        />
                    </Paper>
                </Link>
            </Badge>
        </div>
    )
}

export default (props: any) => {
    const classes = useStyles()
    return <LandingView classes={classes} players={props.players} />
}
