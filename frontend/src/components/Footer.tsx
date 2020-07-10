import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Box, Grid } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    footer: {
        width: '100%',
        padding: theme.spacing(2.1),
        backgroundColor: theme.palette.background.paper,
    },
    affiliationLink: {
        color: 'white',
    }
}));

export default function Footer() {
    const classes = useStyles()
    const discordLink = "https://discord.com/invite/AdB3jey"
    const affiliationLink = "https://www.reddit.com/r/MWLoadouts/"

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
                        {new Date().getFullYear()}{" © FG"}
                    </Typography>
                </Grid>
            </Grid>
            <Box pl={0.35}>
                <Typography variant="body2" color="textSecondary" >
                    {"Affiliated with "}
                    <a href={affiliationLink} className={classes.affiliationLink}>
                        r/MWLoadouts
                    </a>
                </Typography>
            </Box>
        </footer>
    )
}
