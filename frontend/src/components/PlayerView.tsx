import React from "react";
import Api from "../domain/api";
import FormControl from '@material-ui/core/FormControl';
import Grid from '@material-ui/core/Grid';
import InputLabel from '@material-ui/core/InputLabel';
import LinkIcon from "@material-ui/icons/Link";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import Tooltip from '@material-ui/core/Tooltip';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "../domain/player";

interface IProps {
    username: string
    classes: any
}

interface IState {
    player: Player | null
    selectedLoadout: string
}

const useStyles = makeStyles(theme => ({
    container: {
        flexGrow: 1,
        margin: 'auto',
        maxWidth: 1100,
        paddingTop: theme.spacing(2),
        paddingBottom: theme.spacing(2),
    },
    titleGridItem: {
        height: 50,
        margin: 'auto',
        marginBottom: theme.spacing(2),
    },
    title: {
        paddingTop: theme.spacing(0.75),
        fontFamily: 'Bebas Neue',
        fontSize: '2.25rem',
    },
    avatarGridItem: {
        margin: 'auto',
    },
    avatar: {
        borderRadius: '2%',
        height: 290,
        border: '3px solid #555',
        backgroundColor: theme.palette.background.paper,
        [theme.breakpoints.down('sm')]: {
            maxHeight: 230,
        },
    },
    rightColumn: {
        [theme.breakpoints.up('md')]: {
            paddingLeft: theme.spacing(4),
        }
    },
    selectGridItem: {
        height: 50,
        margin: theme.spacing(0, 2, 2, 2),
        [theme.breakpoints.down('sm')]: {
            marginTop: theme.spacing(3),
        },
    },
    formControl: {
        width: '100%',
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
        maxWidth: '100%',
        maxHeight: 50,
    },
    attachmentText: {
        paddingBottom: 2,
    },
    infoContainer: {
        display: 'flex',
        margin: theme.spacing(0, 2, 0, 2),
    },
    lastUpdatedLabel: {
        paddingLeft: theme.spacing(1),
        opacity: '50%',
    }
}));

class PlayerView extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            player: null,
            selectedLoadout: ""
        }
    }

    async getPlayer() {
        const player = await Api.getPlayer(this.props.username)
        this.setState({
            player,
            selectedLoadout: Object.keys(player.loadouts)[0]
        })
    }

    componentDidMount() {
        this.getPlayer().catch(err => console.log(err))
    }

    componentDidUpdate(prevProps: Readonly<IProps>, prevState: Readonly<IState>, snapshot?: any) {
        if (this.props.username !== prevProps.username) {
            this.getPlayer().catch(err => console.log(err))
        }
    }

    onSelectWeapon = (event: any) => {
        this.setState({selectedLoadout: event.target.value})
    };

    render() {
        const player = this.state.player

        if (player == null) {
            return null
        }

        const classes = this.props.classes
        const weapon = this.state.selectedLoadout
        const loadout = player.loadouts[this.state.selectedLoadout]
        const updated = new Date(loadout.lastUpdated)

        return (
            <div className={classes.container}>
                <Grid container alignItems="flex-start">
                    <Grid container direction="column" item xs={12} md={5}>
                        <Grid item className={classes.titleGridItem}>
                            <Typography className={classes.title} variant="h4">
                                {player.username}
                            </Typography>
                        </Grid>
                        <Grid item className={classes.avatarGridItem}>
                            <img className={classes.avatar} src={player.avatar} alt="Avatar "/>
                        </Grid>
                    </Grid>

                    <Grid container className={classes.rightColumn} direction="column" item xs={12} md={7}>
                        <Grid item className={classes.selectGridItem}>
                            <FormControl variant="outlined" className={classes.formControl}>
                                <InputLabel id="loadout-select-label">Loadout</InputLabel>
                                <Select
                                    id="loadout-select"
                                    labelId="loadout-select-label"
                                    label="Loadout"
                                    value={weapon}
                                    onChange={this.onSelectWeapon}
                                >
                                    {Object.keys(player.loadouts).map((weapon) =>
                                        <MenuItem key={weapon} value={weapon}>{weapon}</MenuItem>
                                    )}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item className={classes.listGridItem}>
                            <List classes={{ root: classes.list }}>
                                {Object.entries(loadout.attachments).map(([type, attachment]) => (
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
                        </Grid>
                        <Grid item>
                            <div className={classes.infoContainer}>
                                <Tooltip title="Source">
                                    <a
                                        href={loadout.source}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        <LinkIcon />
                                    </a>
                                </Tooltip>
                                <Typography className={classes.lastUpdatedLabel}>
                                    {`Last updated: ${updated.toLocaleDateString()}`}
                                </Typography>
                            </div>
                        </Grid>
                     </Grid>
                </Grid>
            </div>
        );
    }
}

export default (props: any) => {
    const classes = useStyles()
    return <PlayerView username={props.username} classes={classes} />
}