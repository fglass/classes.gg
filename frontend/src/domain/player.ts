export interface Player {
    username: string;
    avatar: string;
    loadouts: { [loadout: string]: Loadout };
}

export interface Loadout {
    source: string;
    lastUpdated: string,
    attachments: { [type: string]: string };
}