import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Grid } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    footer: {
        backgroundColor: theme.palette.background.paper,
        width: '100%',
        padding: theme.spacing(2.1),
    },
}));

export default function Footer() {
    const classes = useStyles()
    const discordLink = "https://discord.com/invite/AdB3jey"
    return (
        <footer className={classes.footer}>
            <Grid container spacing={1}>
                <Grid item>
                    <a
                        href={discordLink}
                        target="_blank" rel="noopener noreferrer"
                    >
                        <img src={"images/discord.svg"} alt="Discord" width={22} />
                    </a>
                </Grid>
                <Grid item>
                    <Typography variant="body2" color="textSecondary">
                        {new Date().getFullYear()}{' © FG'}
                    </Typography>
                </Grid>
            </Grid>
        </footer>
    )
}
