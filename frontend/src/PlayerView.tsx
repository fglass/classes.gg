import React from "react";
import Api from "./api";
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import { makeStyles } from "@material-ui/core/styles";
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
        paddingTop: theme.spacing(8),
        paddingBottom: theme.spacing(8),
        marginLeft: theme.spacing(8),
    },
    formControl: {
        marginLeft: theme.spacing(4),
        minWidth: 120,
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

        return (
            <div className={classes.container}>
                <h2>{player.username}</h2>
                <img src={player.avatar} alt={"Avatar"}/>

                <FormControl variant="outlined" className={classes.formControl}>
                    <InputLabel id="loadout-select-label">Loadout</InputLabel>
                    <Select
                        id="loadout-select"
                        labelId="loadout-select-label"
                        label="Loadout"
                        value={this.state.selectedWeapon}
                        onChange={this.onSelectWeapon}
                    >
                        {
                            Object.keys(player.weapons).map((weapon) =>
                                <MenuItem key={weapon} value={weapon}>{weapon}</MenuItem>
                            )
                        }
                    </Select>
                  </FormControl>
            </div>
        );
    }
}

export default () => {
    const { username } = useParams();
    const classes = useStyles()
    return <PlayerView username={username} classes={classes}/>
}