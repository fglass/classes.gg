import { makeStyles } from "@material-ui/core/styles";

export const useStyles = makeStyles(theme => ({
    container: {
        flexGrow: 1,
        margin: "auto",
        maxWidth: 750,
        padding: theme.spacing(2),
        paddingBottom: "4rem",
    },
    topContainer: {
        paddingBottom: theme.spacing(2),
    },
    titleGridItem: {
        marginBottom: theme.spacing(2),
        paddingLeft: theme.spacing(2),
    },
    title: {
        paddingTop: theme.spacing(0.75),
        fontFamily: "Bebas Neue",
    },
    subText: {
        paddingBottom: "2px",
        fontSize: "16px",
        color: theme.palette.text.secondary,
    },
    icon: {
        paddingTop: "1px",
        marginRight: "4px",
        fontSize: "16px",
        color: theme.palette.text.secondary,
    },
    avatar: {
        borderRadius: "50%",
        height: 125,
        border: "2px solid #555",
        backgroundColor: theme.palette.background.paper,
    },
    selectGridItem: {
        height: 50,
        marginBottom: theme.spacing(2),
    },
    formControl: {
        width: "100%",
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
    sourcePanel: {
        minHeight: 50,
        backgroundColor: "rgba(66, 66, 66, 0.4)",
        color: theme.palette.text.hint,
        boxShadow: "none",
        marginBottom: theme.spacing(1.25),
    },
    sourcePanelSummary: {
        maxHeight: 40,
    },
    sourceText: {
        color: theme.palette.text.hint,
    },
    link: {
        color: theme.palette.primary.main,
        textDecoration: "none",
        "&:hover": {
            textDecoration: "underline",
        }
    },
}));