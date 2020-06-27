import { Player } from "./player";

export default class Api {

    private static SERVER_URL = "http://192.168.0.46:5000"

    private static async request<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${this.SERVER_URL}/${endpoint}`);
        return await response.json();
    }

    static getPlayer(username: string): Promise<Player> {
        return this.request<Player>(`player/${username}`)
    }

    static getPlayers(): Promise<Array<Player>> {
        return this.request<Array<Player>>("players")
    }
}

