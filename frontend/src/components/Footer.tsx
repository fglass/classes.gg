import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Box, Grid } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    footer: {
        width: "100%",
        padding: theme.spacing(2.1),
        backgroundColor: theme.palette.background.paper,
    },
    affiliationLink: {
        color: "white",
    }
}));

const DiscordLink = () => {
    const discordLink = "https://discord.com/invite/AdB3jey"
    return (
        <a
            href={discordLink}
            target="_blank" rel="noopener noreferrer"
        >
            <img src={"images/discord.svg"} alt="Discord" width={22} />
        </a>
    )
}

const Copyright = () => {
    return (
        <Typography variant="body2" color="textSecondary">
            {new Date().getFullYear()}{" © FG"}
        </Typography>
    )
}

const AffiliationLink = (props: any) => {
    const affiliationLink = "https://www.reddit.com/r/MWLoadouts/"
    return (
        <Typography variant="body2" color="textSecondary" >
            {"Affiliated with "}
            <a href={affiliationLink} className={props.className}>
                r/MWLoadouts
            </a>
        </Typography>
    )
}

export default function Footer() {
    const classes = useStyles()
    return (
        <footer className={classes.footer}>
            <Grid container spacing={1}>
                <Grid item>
                    <DiscordLink />
                </Grid>
                <Grid item>
                    <Copyright />
                </Grid>
            </Grid>
            <Box pl={0.35}>
                <AffiliationLink className={classes.affiliationLink} />
            </Box>
        </footer>
    )
}
