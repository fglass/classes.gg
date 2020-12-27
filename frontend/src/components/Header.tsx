import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { createStyles, fade, makeStyles, Theme } from "@material-ui/core/styles";
import {Grid} from "@material-ui/core";

const useStyles = makeStyles((theme: Theme) => createStyles({
    logo: {
        flexGrow: 1,
        paddingTop: theme.spacing(0.5),
    },
    home: {
        maxWidth: 125,
    },
    title: {
        fontFamily: "Bebas Neue",
        fontSize: "1.57rem",
        paddingLeft: theme.spacing(1.5),
        paddingBottom: theme.spacing(0.125),
    },
}));

const Logo = (props: any) => {
    const classes = props.classes
    return (
         <div className={classes.logo}>
            <a href="/">
                <Grid container className={classes.home} alignItems="center">
                    <Grid item xs={2}>
                        <img src={"images/logo.png"} alt="Logo" />
                    </Grid>
                    <Grid item xs={10}>
                        <Typography className={classes.title}>
                            Classes.gg
                        </Typography>
                    </Grid>
                </Grid>
            </a>
        </div>
    )
}

export default function Header() {
    const classes = useStyles()
    return (
        <div>
            <AppBar position="static">
                <Toolbar>
                    <Logo classes={classes} />
                </Toolbar>
            </AppBar>
        </div>
    )
}
