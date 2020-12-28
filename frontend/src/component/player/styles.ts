import { makeStyles } from "@material-ui/core/styles";

export const useStyles = makeStyles(theme => ({
    container: {
        flexGrow: 1,
        margin: "auto",
        maxWidth: 1100,
        paddingTop: theme.spacing(2),
        paddingBottom: theme.spacing(2),
    },
    titleGridItem: {
        height: 50,
        margin: "auto",
        marginBottom: theme.spacing(2),
    },
    title: {
        paddingTop: theme.spacing(0.75),
        fontFamily: "Bebas Neue",
        fontSize: "2.25rem",
    },
    avatarGridItem: {
        margin: "auto",
    },
    avatar: {
        borderRadius: "2%",
        height: 290,
        border: "3px solid #555",
        backgroundColor: theme.palette.background.paper,
        [theme.breakpoints.down("sm")]: {
            maxHeight: 230,
        },
    },
    rightColumn: {
        [theme.breakpoints.up("md")]: {
            paddingLeft: theme.spacing(4),
        }
    },
    selectGridItem: {
        height: 50,
        margin: theme.spacing(0, 2, 2, 2),
        [theme.breakpoints.down("sm")]: {
            marginTop: theme.spacing(3),
        },
    },
    formControl: {
        width: "100%",
    },
    listGridItem: {
        margin: theme.spacing(0, 2, 0, 2),
    },
    list: {
        padding: 0,
    },
    attachment: {
        borderRadius: 5,
        backgroundColor: theme.palette.background.paper,
        marginBottom: theme.spacing(1.25),
        maxWidth: "100%",
        minHeight: 50,
        maxHeight: 50,
    },
    attachmentText: {
        paddingBottom: 2,
    },
    infoContainer: {
        opacity: "50%",
        display: "flex",
        justifyContent: "space-between",
        margin: theme.spacing(0, 2, 0, 2),
    },
}));