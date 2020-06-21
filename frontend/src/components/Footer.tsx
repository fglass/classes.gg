import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(theme => ({
    footer: {
        backgroundColor: theme.palette.background.paper,
        width: '100%',
        marginTop: theme.spacing(2),
        padding: theme.spacing(4),
        [theme.breakpoints.up('md')]: {
            position: 'fixed',
            bottom: 0,
        },
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
