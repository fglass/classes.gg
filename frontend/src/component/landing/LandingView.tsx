import React from "react";
import TimeAgo from 'timeago-react';
import InputBase from "@material-ui/core/InputBase";
import SearchIcon from "@material-ui/icons/Search";
import Typography from "@material-ui/core/Typography";
import { Badge, Icon, Paper } from "@material-ui/core";
import { Link } from "react-router-dom";
import { Player } from "../../model/player";
import { useStyles } from "./styles";
import {Alert} from "@material-ui/lab";

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

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.players !== prevProps.players) {
            this.setState({
                filteredPlayers: this.props.players,
            })
        }
    }

    onSearch = (input: string) => {
        this.setState({
            filteredPlayers: this.props.players.filter(player => this.isSearchMatch(player, input))
        })
    }

    isSearchMatch = (player: Player, input: string) => (
        player.username.toLowerCase().startsWith((input)) ||
        player.loadoutKeys.some(key => key.toLowerCase().includes(input))
    )


    render() {
        const { classes, players } = this.props
        const nLoadouts = players.reduce((sum, player) => sum + player.loadoutKeys.length, 0)
        return (
            <div className={classes.content}>
                <div className={classes.header}>
                    <Typography className={classes.heading}>
                        Classes<span className={classes.primaryColour}>.</span>gg
                    </Typography>
                    <Typography className={classes.subheading}>
                        Call of Duty: Warzone Loadout Repository
                    </Typography>
                    <Typography className={classes.subheading}>
                        <span className={classes.highlightText}>{nLoadouts}</span> Loadouts
                        from <span className={classes.highlightText}>{players.length}</span> Players
                    </Typography>
                    <SearchInput classes={classes} onSearch={this.onSearch} />
                </div>
                <div>
                    <Alert variant="filled" severity="info" className={classes.alert}>
                        Loadouts are now auto-updated hourly!
                    </Alert>
                    <div className={classes.grid}>
                        {this.state.filteredPlayers.map(player =>
                            <PlayerCard classes={classes} player={player} key={player.username} />
                        )}
                    </div>
                    <YouTubeEmbed classes={classes} />
                </div>
            </div>
        )
    }
}

const SearchInput = (props: any) => {
    const classes = props.classes
    return (
        <div className={classes.search}>
            <div className={classes.searchIcon}>
                <SearchIcon />
            </div>
            <InputBase
                placeholder="Search player or loadout"
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
            <Badge
                color="primary"
                classes={{anchorOriginTopRightRectangle: classes.badgePosition}}
                badgeContent={player.loadoutKeys.length}
            >
                <Link to={`/${player.username}`}>
                    <Paper className={classes.card} variant="outlined">
                        <img className={classes.avatar} src={player.avatar} alt="" />
                        <Typography>{player.username}</Typography>
                        <Icon className={classes.calendarIcon}>calendar_today</Icon>
                        <TimeAgo className={classes.timeAgo} datetime={player.lastUpdated + " UTC"} live={false} />
                    </Paper>
                </Link>
            </Badge>
        </div>
    )
}

const EMBED_ID = "g3_IDtnoLBA"

const YouTubeEmbed = (props: any) => {
    const classes = props.classes
    return (
        <div className={classes.embed}>
            <iframe
                className={classes.iframe}
                title="Embedded video"
                src={`https://www.youtube.com/embed/${EMBED_ID}`}
                frameBorder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
            />
        </div>
    )
}

export default (props: any) => {
    const classes = useStyles()
    return <LandingView classes={classes} players={props.players} />
}
