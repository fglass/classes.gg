import { LoadoutMap, Player } from "./player";

export default class Api {

    private static SERVER_URL = process.env.NODE_ENV === "production" ? "/api" : "http://localhost:5000/api"

    static getPlayers(): Promise<Array<Player>> {
        return this.request<Array<Player>>("players")
    }

    static getLoadoutsForPlayer(player: Player): Promise<LoadoutMap> {
        return this.request<LoadoutMap>(`loadouts/${player.username}`)
    }

    private static async request<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${this.SERVER_URL}/${endpoint}`);
        return await response.json();
    }
}

