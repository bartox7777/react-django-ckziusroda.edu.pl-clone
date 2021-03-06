import { combineReducers } from "redux";
import news from "./news";
import posts from "./posts";
import authentication from "./authentication";
import alerts from "./alerts";
import categories from "./categories";
import files from "./files";

export default combineReducers({
  news,
  posts,
  authentication,
  alerts,
  categories,
  files,
});
