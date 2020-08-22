import React from "react";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Box } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    footer: {
        width: "100%",
        padding: theme.spacing(2.1),
        backgroundColor: theme.palette.background.paper,
    },
    link: {
        color: "white",
    }
}));

const Copyright = (props: any) => {
    const contactLink = "https://fred.glass/"
    return (
        <Typography variant="body2" color="textSecondary">
            {new Date().getFullYear()}{" © "}<a href={contactLink} className={props.className}>FG</a>
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
            <Box pl={0.35}>
                <Copyright className={classes.link} />
            </Box>
            <Box pl={0.35}>
                <AffiliationLink className={classes.link} />
            </Box>
        </footer>
    )
}
