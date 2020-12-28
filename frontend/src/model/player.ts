export interface Player {
    username: string;
    avatar: string;
    lastUpdated: string;
    nLoadouts: number;
}

export interface Loadout {
    game: string;
    source: string;
    attachments: { [type: string]: string };
}

export type LoadoutMap = { [loadout: string]: Loadout }