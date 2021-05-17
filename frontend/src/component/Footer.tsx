import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import {Button, Grid} from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    footer: {
        position: "absolute",
        bottom: 0,
        width: "100%",
        height: "4rem",
        padding: theme.spacing(1.5),
        backgroundColor: theme.palette.background.paper,
    },
    link: {
        color: "white",
    }
}));

const Copyright = (props: any) => {
    const contactLink = "https://fred.glass/"
    const copyright = `${new Date().getFullYear()}  © `
    return (
        <Typography variant="body2" color="textSecondary">
            {copyright}
            <a href={contactLink} target="_blank" rel="noopener noreferrer" className={props.className}>
                Fred Glass
            </a>
        </Typography>
    )
}

const SupportButton = () => {
    const supportLink = "https://www.buymeacoffee.com/classesgg"
    return (
        <Button variant="outlined" size="small" href={supportLink} target="_blank" rel="noopener noreferrer">
            <span role="img" aria-label="Coffee">☕ Support</span>
        </Button>
    )
}

export default function Footer() {
    const classes = useStyles()
    return (
        <footer className={classes.footer}>
            <Grid container justify="space-between">
                <Grid item>
                    <Copyright className={classes.link} />
                    <Typography variant="body2" color="textSecondary">
                        Not affiliated with Activision
                    </Typography>
                </Grid>
                <Grid item>
                   <SupportButton />
                </Grid>
            </Grid>
        </footer>
    )
}
