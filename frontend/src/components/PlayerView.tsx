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
import Typography from "@material-ui/core/Typography";
import UpdateIcon from '@material-ui/icons/Update';
import { makeStyles } from "@material-ui/core/styles";
import { Loadout, Player } from "../model/player";
import { SEO } from "./SEO";

interface IProps {
    classes: any
    player: Player
}

interface IState {
    selectedLoadout: string
}

const useStyles = makeStyles(theme => ({
    container: {
        flexGrow: 1,
        margin: "auto",
        maxWidth: 1100,
        paddingTop: theme.spacing(2),
        paddingBottom: theme.spacing(2),
    },
    titleGridItem: {
        height: 50,
        margin: "auto",
        marginBottom: theme.spacing(2),
    },
    title: {
        paddingTop: theme.spacing(0.75),
        fontFamily: "Bebas Neue",
        fontSize: "2.25rem",
    },
    avatarGridItem: {
        margin: "auto",
    },
    avatar: {
        borderRadius: "2%",
        height: 290,
        border: "3px solid #555",
        backgroundColor: theme.palette.background.paper,
        [theme.breakpoints.down("sm")]: {
            maxHeight: 230,
        },
    },
    rightColumn: {
        [theme.breakpoints.up("md")]: {
            paddingLeft: theme.spacing(4),
        }
    },
    selectGridItem: {
        height: 50,
        margin: theme.spacing(0, 2, 2, 2),
        [theme.breakpoints.down("sm")]: {
            marginTop: theme.spacing(3),
        },
    },
    formControl: {
        width: "100%",
    },
    listGridItem: {
        margin: theme.spacing(0, 2, 0, 2),
    },
    list: {
        padding: 0,
    },
    attachment: {
        borderRadius: 5,
        backgroundColor: theme.palette.background.paper,
        marginBottom: theme.spacing(1.25),
        maxWidth: "100%",
        minHeight: 50,
        maxHeight: 50,
    },
    attachmentText: {
        paddingBottom: 2,
    },
    infoContainer: {
        opacity: "50%",
        display: "flex",
        justifyContent: "space-between",
        margin: theme.spacing(0, 2, 0, 2),
    },
}));

interface LoadoutDropdownProps {
    className: string;
    selectedWeapon: String;
    onSelectWeapon: (event: any) => void;
    loadouts: { [weapon: string]: Loadout };
}

const LoadoutDropdown = (props: LoadoutDropdownProps) => {
    const { className, selectedWeapon, onSelectWeapon, loadouts } = props
    return (
        <FormControl variant="outlined" className={className}>
            <InputLabel id="loadout-select-label">Loadout</InputLabel>
            <Select
                id="loadout-select"
                labelId="loadout-select-label"
                label="Loadout"
                value={selectedWeapon}
                onChange={onSelectWeapon}
            >
                {Object.entries(loadouts).map(([weapon, loadout]) => (
                    <MenuItem key={weapon} value={weapon} style={{display: "block"}}>
                        <Typography variant="inherit">{weapon}</Typography>
                        <div style={{float: "right", paddingRight: "5px"}}>
                            <img src={`images/${loadout.origin.toLowerCase()}.svg`} alt="" style={{opacity: 0.5}} />
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

const LoadoutInformation = (props: any) => {
    const { classes, source, lastUpdated } = props
    return (
        <div className={classes.infoContainer}>
            <div style={{"display": "flex"}}>
                <UpdateIcon />
                <Typography style={{"paddingLeft": "4px"}}>
                    {lastUpdated.toLocaleDateString()}
                </Typography>
            </div>
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
            selectedLoadout: ""
        }
    }

    private static N_ATTACHMENTS = 5

    setDefaultLoadout() {
        this.setState({
            selectedLoadout: Object.keys(this.props.player.loadouts)[0]
        })
    }

    componentDidMount() {
        this.setDefaultLoadout()
    }

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.player !== prevProps.player) {
            this.setDefaultLoadout()
        }
    }

    onSelectWeapon = (event: any) => {
        this.setState({selectedLoadout: event.target.value})
    };

    render() {
        const player = this.props.player

        if (player == null) {
            return null
        }

        const classes = this.props.classes
        const weapon = this.state.selectedLoadout
        const loadout = player.loadouts[this.state.selectedLoadout]

        if (loadout == null) {
            return null
        }

        const lastUpdated = new Date(player.lastUpdated)
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
            <div className={classes.container}>
                <SEO username={player.username} date={lastUpdated} />
                <Grid container alignItems="flex-start">

                    <Grid container direction="column" item xs={12} md={5}>
                        <Grid item className={classes.titleGridItem}>
                            <Typography className={classes.title} variant="h4">
                                {player.username}
                            </Typography>
                        </Grid>
                        <Grid item className={classes.avatarGridItem}>
                            <img className={classes.avatar} src={player.avatar} alt="Avatar" />
                        </Grid>
                    </Grid>

                    <Grid container className={classes.rightColumn} direction="column" item xs={12} md={7}>
                        <Grid item className={classes.selectGridItem}>
                            <LoadoutDropdown
                                className={classes.formControl}
                                selectedWeapon={weapon}
                                onSelectWeapon={this.onSelectWeapon}
                                loadouts={player.loadouts}
                            />
                        </Grid>
                        <Grid item className={classes.listGridItem}>
                            <AttachmentList classes={classes} attachments={attachments} />
                        </Grid>
                        <Grid item>
                            <LoadoutInformation classes={classes} source={loadout.source} lastUpdated={lastUpdated} />
                        </Grid>
                     </Grid>
                </Grid>
            </div>
        );
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <PlayerView classes={classes} player={props.player} />
}