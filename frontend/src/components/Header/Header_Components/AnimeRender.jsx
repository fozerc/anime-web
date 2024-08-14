export const AnimeRender = ({data}) => {
    return data.map((anime) => (
        <div>
            {anime.name}
            {anime.year_of_issue}
            <img src={anime.photo} alt=""/>
        </div>
    ))
}