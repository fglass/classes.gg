import React from "react";
import Api from "../domain/api";
import FormControl from '@material-ui/core/FormControl';
import Grid from '@material-ui/core/Grid';
import InputLabel from '@material-ui/core/InputLabel';
import LinkIcon from "@material-ui/icons/Link";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import Tooltip from '@material-ui/core/Tooltip';
import Typography from '@material-ui/core/Typography';
import UpdateIcon from "@material-ui/icons/Update";
import { makeStyles } from "@material-ui/core/styles";
import { Player } from "../domain/player";

interface IProps {
    username: string
    classes: any
}

interface IState {
    player: Player | null
    selectedWeapon: string
}

const useStyles = makeStyles(theme => ({
    container: {
        paddingTop: theme.spacing(10),
        margin: 'auto',
        width: '50%',
    },
    title: {
        paddingTop: theme.spacing(0.75),
        fontFamily: 'Bebas Neue',
        fontSize: '2.25rem',
    },
    firstRow: {
        height: 75,
    },
    secondRow: {
        height: 300,
    },
    avatar: {
        borderRadius: '2%',
    },
    formControl: {
        minWidth: '100%',
    },
    list: {
        padding: 0,
    },
    attachment: {
        borderRadius: 5,
        backgroundColor: theme.palette.background.paper,
        marginBottom: theme.spacing(1.9),
        maxWidth: '100%',
        maxHeight: 50,
    },
    iconContainer: {
        paddingTop: theme.spacing(1),
    },
    sourceIcon: {
        color: "#FFF",
        paddingRight: theme.spacing(1),
    },
    sourceIconTooltip: {
        paddingLeft: theme.spacing(1),
    }
}));

class PlayerView extends React.Component<IProps, IState> {
    constructor(props: IProps) {
        super(props);
        this.state = {
            player: null,
            selectedWeapon: ""
        }
    }

    async getPlayer() {
        const player = await Api.getPlayer(this.props.username)
        this.setState({
            player,
            selectedWeapon: Object.keys(player.weapons)[0]
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
        this.setState({selectedWeapon: event.target.value})
    };

    render() {
        const player = this.state.player

        if (player == null) {
            return null
        }

        const classes = this.props.classes
        const weapon = this.state.selectedWeapon
        const attachments = Object.values(player.weapons[this.state.selectedWeapon])

        return (
            <div className={classes.container}>
                <Grid container>
                    <Grid item xs={12} md={5} container direction="column">
                        <Grid item className={classes.firstRow} style={{width: 300}}>
                            <Typography className={classes.title} variant="h4" align="center">
                                {player.username}
                            </Typography>
                        </Grid>
                        <Grid item className={classes.secondRow} style={{width: 300}}>
                            <img className={classes.avatar} src={player.avatar} alt={"Avatar"} />
                        </Grid>
                        <Grid item>
                            <div className={classes.iconContainer}>
                                <Tooltip title="Last updated: 20/06/2020">
                                    <UpdateIcon />
                                </Tooltip>
                                <Tooltip title="Source" className={classes.sourceIconTooltip}>
                                    <a
                                        className={classes.sourceIcon}
                                        href="http://www.twitch.tv/scump"
                                        target="_blank" rel="noopener noreferrer"
                                    >
                                        <LinkIcon />
                                    </a>
                                </Tooltip>
                            </div>
                        </Grid>
                    </Grid>

                    <Grid item xs={12} md={7} container direction="column" >
                        <Grid item className={classes.firstRow}>
                            <FormControl variant="outlined" className={classes.formControl}>
                                <InputLabel id="loadout-select-label">Loadout</InputLabel>
                                <Select
                                    id="loadout-select"
                                    labelId="loadout-select-label"
                                    label="Loadout"
                                    value={weapon}
                                    onChange={this.onSelectWeapon}
                                >
                                    {Object.keys(player.weapons).map((weapon) =>
                                        <MenuItem key={weapon} value={weapon}>{weapon}</MenuItem>
                                    )}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item className={classes.secondRow}>
                            <List classes={{ root: classes.list }}>
                                {attachments.map((attachment, index) =>
                                    <ListItem key={index} className={classes.attachment}>
                                        <ListItemText primary={attachment} />
                                    </ListItem>
                                )}
                            </List>
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