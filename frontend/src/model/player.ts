export interface Player {
    username: string;
    avatar: string;
    views: number;
    lastUpdated: string;
    loadoutKeys: Array<String>;
}

export interface Loadout {
    attachments: { [type: string]: string };
    game: string;
    lastUpdated: string;
    source: string;
    sourceUrl: string;
}

export type LoadoutMap = { [loadout: string]: Loadout }