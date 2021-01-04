import React from "react";
import FormControl from "@material-ui/core/FormControl";
import Grid from "@material-ui/core/Grid";
import InputLabel from "@material-ui/core/InputLabel";
import LinkIcon from "@material-ui/icons/Link";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";
import Tooltip from "@material-ui/core/Tooltip";
import TimeAgo from "timeago-react";
import Typography from "@material-ui/core/Typography";
import Api from "../../model/api";
import { Loadout, LoadoutMap, Player } from "../../model/player";
import { SEO } from "../SEO";
import { useStyles } from "./styles";
import { Icon } from "@material-ui/core";

interface IProps {
    classes: any
    className: string
    player: Player
}

interface IState {
    loadouts: LoadoutMap;
    selectedLoadout: string
}

interface LoadoutDropdownProps {
    className: string;
    selectedLoadout: String;
    onSelectLoadout: (event: any) => void;
    loadouts: { [weapon: string]: Loadout };
}

const LoadoutDropdown = (props: LoadoutDropdownProps) => {
    const { className, selectedLoadout, onSelectLoadout, loadouts } = props
    return (
        <FormControl variant="outlined" className={className}>
            <InputLabel id="loadout-select-label">Loadout</InputLabel>
            <Select
                id="loadout-select"
                labelId="loadout-select-label"
                label="Loadout"
                value={selectedLoadout}
                onChange={onSelectLoadout}
            >
                {Object.entries(loadouts).map(([weapon, loadout]) => (
                    <MenuItem key={weapon} value={weapon} style={{display: "block"}}>
                        <Typography variant="inherit">{weapon.replace(" CW", "")}</Typography>
                        <div style={{float: "right", paddingRight: "5px"}}>
                            <img src={`images/${loadout.game.toLowerCase()}.svg`} alt="" style={{opacity: 0.5}} />
                        </div>
                    </MenuItem>
                ))}
            </Select>
        </FormControl>
    )
}

const AttachmentList = (props: any) => {
    const { classes, attachments } = props
    return (
        <List classes={{ root: classes.list }}>
            {attachments.map(([type, attachment]: [string, string]) => (
                <ListItem className={classes.attachment} key={type}>
                    <div className={classes.attachmentText}>
                        <Typography variant="caption" color="textSecondary">
                            {type}
                        </Typography>
                        <Typography>{attachment}</Typography>
                    </div>
                </ListItem>
            ))}
        </List>
    )
}

const SourceIcon = (props: any) => {
    const { classes, source } = props
    return (
        <div className={classes.source}>
            <Tooltip title="Source">
                <a href={source} target="_blank" rel="noopener noreferrer">
                    <LinkIcon />
                </a>
            </Tooltip>
        </div>
    )
}

class PlayerView extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            loadouts: {},
            selectedLoadout: ""
        }
    }

    private static N_ATTACHMENTS = 5

    async getLoadoutsForPlayer() {
        const loadouts = await Api.getLoadoutsForPlayer(this.props.player)
        this.setState({
            loadouts: loadouts,
            selectedLoadout: Object.keys(loadouts)[0]
        })
    }

    componentDidMount() {
        this.getLoadoutsForPlayer().catch(err => console.log(err))
    }

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.player !== prevProps.player) {
            this.getLoadoutsForPlayer().catch(err => console.log(err))
        }
    }

    onSelectLoadout = (event: any) => {
        this.setState({selectedLoadout: event.target.value})
    };

    render() {
        const { player, classes, className } = this.props

        if (player == null) {
            return <div className={className} />
        }

        const { loadouts, selectedLoadout } = this.state

        const loadout = loadouts[selectedLoadout]

        if (loadout == null) {
            return <div className={className} />
        }

        const keys = Object.keys(loadout.attachments)
        const attachments: Array<[string, string]> = []

        // Validate attachments
        for (let i = 0; i < PlayerView.N_ATTACHMENTS; i++) {
            if (i < keys.length) {
                const key = keys[i];
                attachments.push([key, loadout.attachments[key]])
            } else{
                attachments.push(["", ""]) // Empty slot
            }
        }

        return (
            <div className={className}>
                <SEO username={player.username} date={new Date(player.lastUpdated).toISOString()} />
                <div className={classes.container}>
                    <Grid container alignItems="flex-start">

                        <Grid container item className={classes.topContainer}>
                             <Grid item>
                                <img className={classes.avatar} src={player.avatar} alt="Avatar" />
                            </Grid>
                            <Grid item className={classes.titleGridItem}>
                                <Typography className={classes.title} variant="h4">
                                    {player.username}
                                </Typography>
                                <Typography className={classes.subText}>
                                    <Icon className={classes.icon}>apps</Icon>
                                    {`${player.loadoutKeys.length} Loadouts`}
                                </Typography>
                                <Icon className={classes.icon}>calendar_today</Icon>
                                <TimeAgo className={classes.subText} datetime={player.lastUpdated} live={false} />
                            </Grid>
                        </Grid>

                        <Grid container direction="column" item>
                            <Grid item className={classes.selectGridItem}>
                                <LoadoutDropdown
                                    className={classes.formControl}
                                    selectedLoadout={selectedLoadout}
                                    onSelectLoadout={this.onSelectLoadout}
                                    loadouts={loadouts}
                                />
                            </Grid>
                            <Grid item>
                                <AttachmentList classes={classes} attachments={attachments} />
                            </Grid>
                            <Grid item>
                                <SourceIcon classes={classes} source={loadout.source} />
                            </Grid>
                         </Grid>
                    </Grid>
                </div>
            </div>
        );
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <PlayerView classes={classes} className={props.className} player={props.player} />
}