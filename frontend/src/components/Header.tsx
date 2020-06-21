import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from "@material-ui/core/Typography";
import {makeStyles} from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    title: {
        paddingTop: theme.spacing(0.5),
        paddingLeft: theme.spacing(1),
        fontFamily: 'Bebas Neue',
        fontSize: '1.52rem',
    },
}));

export default function Header() {
    const classes = useStyles()
    return (
        <AppBar position="relative">
            <Toolbar>
                <img src={"/images/logo.svg"} alt="Classes.gg" />
                <Typography className={classes.title}>
                    Classes.gg
                </Typography>
            </Toolbar>
        </AppBar>
    )
}
