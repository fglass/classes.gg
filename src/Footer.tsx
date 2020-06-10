import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
    footer: {
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(4),
    },
}));

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary">
            {new Date().getFullYear()}{' © FG.'}
        </Typography>
    );
}

export default function Footer() {
    const classes = useStyles();
    return (
        <footer className={classes.footer}>
            <Copyright />
            <Typography variant="body2" color="textSecondary" component="p">
                Activision has not endorsed and is not responsible for this site or its content.
            </Typography>
        </footer>
    )
}
