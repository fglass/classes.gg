import React from "react";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import FormControl from "@material-ui/core/FormControl";
import Grid from "@material-ui/core/Grid";
import Icon from "@material-ui/core/Icon";
import InputLabel from "@material-ui/core/InputLabel";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";
import TimeAgo from "timeago-react";
import Typography from "@material-ui/core/Typography";
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import Api from "../../model/api";
import { Loadout, LoadoutMap, Player } from "../../model/player";
import { SEO } from "../SEO";
import { useStyles } from "./styles";

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

const SourcePanel = (props: any) => {
    const { classes, loadout } = props
    return (
         <ExpansionPanel className={classes.sourcePanel}>
            <ExpansionPanelSummary
                classes={{expanded: classes.sourcePanelSummary}}
                expandIcon={<ArrowDropDownIcon />}
                aria-controls="source-content"
                id="source-header"
            >
                <Typography>Source</Typography>
            </ExpansionPanelSummary>
            <ExpansionPanelSummary>
                <Grid container>
                    <Grid item>
                        <Typography className={classes.sourceText} variant="caption">
                            {loadout.source}
                        </Typography>
                    </Grid>
                    <Grid item>
                        <Typography className={classes.sourceText} variant="caption">
                            Updated from{' '}
                                <a
                                    href={loadout.sourceUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className={classes.link}
                                >
                                    {loadout.sourceUrl.includes("twitch") ? "Twitch" : "Google Sheets"}
                                </a>
                            {' '}at {new Date(loadout.lastUpdated).toISOString()}
                        </Typography>
                    </Grid>
                </Grid>
            </ExpansionPanelSummary>
        </ExpansionPanel>
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

    onLoad() {
        if (this.props.player != null) {
            this.getLoadoutsForPlayer().catch(err => console.log(err))
            Api.viewPlayer(this.props.player)
        }
    }

    async getLoadoutsForPlayer() {
        const loadouts = await Api.getLoadoutsForPlayer(this.props.player)
        this.setState({
            loadouts: loadouts,
            selectedLoadout: Object.keys(loadouts)[0]
        })
    }

    componentDidMount() {
        this.onLoad()
    }

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.player !== prevProps.player) {
            this.onLoad()
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
                attachments.push(["", "Empty"])
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
                                    <Icon className={classes.icon}>visibility</Icon>
                                    {`${player.views} views`}
                                </Typography>
                                <Icon className={classes.icon}>calendar_today</Icon>
                                <TimeAgo className={classes.subText} datetime={player.lastUpdated + " UTC"} live={false} />
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
                                <SourcePanel classes={classes} loadout={loadout} />
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