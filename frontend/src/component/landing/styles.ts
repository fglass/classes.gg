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
        textAlign: "center",
        height: "110px",
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
    search: {
        position: "relative",
        borderRadius: theme.shape.borderRadius,
        backgroundColor: fade(theme.palette.common.white, 0.15),
        "&:hover": {
            backgroundColor: fade(theme.palette.common.white, 0.25),
        },
        width: "81%",
        maxWidth: "400px",
        margin: "auto",
        marginTop: "20px",
        border: "1px solid",
        borderColor: "rgba(255, 255, 255, 0.12)",
    },
    searchIcon: {
        padding: theme.spacing(0, 2),
        height: "100%",
        position: "absolute",
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
        padding: theme.spacing(1, 1, 1, 0),
        paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
        transition: theme.transitions.create("width"),
    },
    grid: {
        maxWidth: "1050px",
        width: "100%",
        margin: "0px auto",
        display: "grid",
        gap: "15px",
        gridTemplateColumns: "repeat(auto-fit, minmax(160px, 1fr))",
        justifyItems: "center",
        padding: "25px 0px",
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
}));