import React from "react";
import Api from "./api";
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import { makeStyles } from "@material-ui/core/styles";
import { List, ListItem, ListItemText } from "@material-ui/core";
import { useParams } from "react-router";
import { Player } from "./player";


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
        marginLeft: theme.spacing(8),
    },
    formControl: {
        marginLeft: theme.spacing(4),
        minWidth: 120,
    },
    attachment: {
        borderRadius: 5,
        backgroundColor: theme.palette.background.paper,
        marginBottom: theme.spacing(4),
        maxWidth: '50%',
    },
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
        this.setState({player: await Api.getPlayer(this.props.username)})
    }

    componentDidMount() {
        this.getPlayer().catch(err => console.log(err))
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
        const attachments = weapon !== "" ? Object.values(player.weapons[this.state.selectedWeapon]) : ['', '', '', '', '']

        return (
            <div className={classes.container}>
                <h1>{player.username}</h1>
                <img src={player.avatar} alt={"Avatar"}/>

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

                <List>
                    {attachments.map((attachment, index) =>
                        <ListItem key={index} className={classes.attachment}>
                          <ListItemText primary={attachment} />
                        </ListItem>
                    )}
                 </List>
            </div>
        );
    }
}

export default () => {
    const { username } = useParams();
    const classes = useStyles()
    return <PlayerView username={username} classes={classes}/>
}