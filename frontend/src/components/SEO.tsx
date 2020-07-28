import React from "react";
import { Helmet } from "react-helmet";

export const SEO = (props: any) => {
    const { username, date } = props
    let title = "Classes.gg - Warzone Loadout Repository"
    let description = "View Call of Duty: Warzone loadouts from professional players, streamers and other content creators"
    let url = "https://www.classes.gg"

    if (window.location.pathname !== "/") {
        title = `Classes.gg - ${username} Warzone Loadouts`
        description = `View Call of Duty: Warzone loadouts of ${username}`
        url = `https://www.classes.gg/${username}`
    }

    const structuredData = `{
        "@context": "http://schema.org",
        "@type": "WebApplication",
        "name": "Classes.gg",
        "url": "${url}",
        "description": "${description}",
        "applicationCategory": "Game",
        "applicationSubCategory": "Game Information",
        "about": {
            "@type": "Thing",
            "description": "warzone, loadout, weapon, streamer, youtuber"
        },
        "browserRequirements": "Requires JavaScript",
        "softwareVersion": "1.0.0",
        "operatingSystem": "All",
        "datePublished": "${date}",
        "dateModified": "${date}",
    }`

    return (
        <Helmet>
            <title>{title}</title>
            <meta name="description" content={description} />

            <meta
                name="image"
                content="https://classes.gg/images/logo.svg"
            />

            <meta property="og:url" content={url} />
            <meta
                property="og:type"
                content="SoftwareApplication"
            />
            <meta
                property="og:title"
                content={title}
            />
            <meta
                property="og:description"
                content={description}
            />
            <meta
                property="og:image"
                content="https://classes.gg/images/logo.svg"
            />
            <meta
                name="article:published_time"
                content={date}
            />

            <script type="application/ld+json">
                {structuredData}
            </script>

            <meta name="author" content="FG" />
            <html lang="en" dir="ltr" />
        </Helmet>
    )
}