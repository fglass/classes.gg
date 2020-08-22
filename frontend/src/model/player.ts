export interface Player {
    username: string;
    avatar: string;
    lastUpdated: string;
    loadouts: { [loadout: string]: Loadout };
}

export interface Loadout {
    source: string;
    attachments: { [type: string]: string };
}