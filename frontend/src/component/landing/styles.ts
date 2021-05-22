import { createStyles, fade, makeStyles, Theme } from "@material-ui/core/styles";

export const useStyles = makeStyles((theme: Theme) => createStyles({
    content: {
        paddingBottom: "4rem",
    },
    header: {
        paddingBottom: theme.spacing(3),
        paddingTop: theme.spacing(1),
        backgroundColor: theme.palette.background.paper,
    },
    heading: {
        fontFamily: "Bebas Neue",
        fontSize: "6rem",
        height: "110px",
        textAlign: "center",
        [theme.breakpoints.down("sm")]: {
            fontSize: "5rem",
            height: "100px",
        },
    },
    primaryColour: {
        color: theme.palette.primary.main,
    },
    subheading: {
        textAlign: "center",
        color: theme.palette.text.secondary,
    },
    highlightText: {
        color: theme.palette.primary.main,
    },
    search: {
        position: "relative",
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        "&:hover": {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        maxWidth: "450px",
        width: "90%",
        margin: "auto",
        marginTop: "15px",
        border: "1px solid",
        borderColor: "rgba(255, 255, 255, 0.12)",
    },
    searchIcon: {
        height: "100%",
        position: "absolute",
        right: theme.spacing(2),
        pointerEvents: "none",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },
    inputRoot: {
        width: "100%",
        color: "inherit",
    },
    input: {
        padding: theme.spacing(1, 1, 1, 2),
        height: "25px",
        transition: theme.transitions.create("width"),
    },
    grid: {
        maxWidth: "1050px",
        width: "90%",
        margin: "0px auto",
        display: "grid",
        gap: "15px",
        gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))",
        justifyItems: "center",
        padding: "10px 0px 15px 0px",
    },
    card: {
        width: "160px",
        height: "147px",
        borderRadius: "7px",
        textAlign: 'center',
        padding: theme.spacing(2),
        color: theme.palette.text.primary,
        "&:hover": {
            backgroundColor: theme.palette.primary.dark,
            borderColor: theme.palette.primary.main
        }
    },
    avatar: {
        width: "60px",
        height: "60px",
        borderRadius: "60px",
        marginBottom: theme.spacing(1),
    },
    timeAgo: {
        paddingBottom: "2px",
        fontSize: "14px",
        color: theme.palette.text.secondary,
    },
    calendarIcon: {
        paddingTop: "1px",
        marginRight: "4px",
        fontSize: "14px",
        color: theme.palette.text.secondary,
    },
    alert: {
        margin: "auto",
        marginTop: "10px",
        maxWidth: "1050px",
        width: "90%",
    },
    embed: {
        maxWidth: "1050px",
        width: "90%",
        margin: "0px auto",
        paddingTop: "10px",
    },
    iframe: {
        width: "100%",
        border: "1px solid rgba(255, 255, 255, 0.12)",
        borderRadius: "7px",
    }
}));